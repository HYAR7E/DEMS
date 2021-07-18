""" Google Drive API dependences """
# Build function to create a service
from googleapiclient.discovery import build
# To upload files
from googleapiclient.http import MediaFileUpload
import mimetypes
# Service account
from google.oauth2 import service_account
# Configuración del proyecto
from django.conf import settings


SCOPES = ['https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = str(settings.BASE_DIR)+str(settings.STATIC_URL)+'gdrive/credentials.json'


class GAPIDRIVE:
    """ Google Drive API """
    def __init__(self):
        # Set credentials from file
        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        #print("credentials")
        # Initializate gapi drive service
        service = build('drive', 'v3', credentials=credentials)
        #print("service")
        # Add service as a propertie
        self.service = service
    # Get all files from drive
    def get_files(self):
        results = self.service.files().list(
            fields="files(id, name, mimeType, size, webViewLink, webContentLink, parents)",
        ).execute()
        # Default pagesize: 100
        files = results.get('files', [])
        return files
    # Get files by folder id
    def get_files_from_folder(self, folder_id):
        query = "'%s' in parents" % folder_id
        results = self.service.files().list(
            q=query,
            fields="files(id, name, mimeType, size, webViewLink, webContentLink, parents)",
        ).execute()
        files = results.get('files', [])
        return files
    # Print files formated at CLI
    def print_files(self, files):
        if not files:
            print('No files found.')
        else:
            #print('Files:')
            for item in files:
                print(u'{0} tipo:{1} peso:{2} id:{3}'.format(
                    item.get('name'),
                    item.get('mimeType').split('.')[-1],
                    item.get('size') if item.get('size') else 0,
                    item.get('id'),
                ))
    # Create a folder
    def create_folder(self, name, make_public=True):
        file = self.service.files().create(
            body={
                'name': name,
                'mimeType': 'application/vnd.google-apps.folder'
            },
            fields='id'
        ).execute()

        # Make this folder as public
        if make_public:
            self.make_public(file.get('id'))

        return file.get('id')
    # Create file inside folder
    def create_file(self, filepath, name, parent_folder_id=None):
        # Get file's data
        #print("File data")
        mimetype = mimetypes.guess_type(filepath)[0]
        file_metadata = {'name': name}
        if parent_folder_id:
            file_metadata['parents'] = [parent_folder_id]
        #print("file_metadata: %s" % file_metadata)
        # Upload file stream
        #print("File stream")
        media = MediaFileUpload(filepath, mimetype=mimetype)
        # Create file
        #print("Create file")
        file = self.service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, name, webViewLink, webContentLink'
        ).execute()
        return file
    # Set file's permission to public
    def make_public(self, file_id):
        self.service.permissions().create(
            fileId=file_id,
            body={
                'type': 'anyone',
                'role': 'reader',
            },
            fields='id'
        ).execute()
    # Delete file
    def delete_file(self, file_id):
        self.service.files().delete(fileId=file_id).execute()
    def get_meta_usage(self):
        return self.service.about().get(fields="storageQuota").execute()


""" Ejemplos
# Crear objeto gapidrive
gadrive = GAPIDRIVE()

# Obtener e imprimir todos los archivos
files = gadrive.get_files()
gadrive.print_files(files)

# Crear carpeta y subir un archivo a la carpeta creada
folder_id = gadrive.create_folder("container_1")
file_id = gadrive.create_file("secret.txt", "secreto.txt", folder_id)

# Hacer publico un archivo o carpeta
gadrive.make_public(file_id)

# Flujo basico completo
folder_id = gadrive.create_folder("nueva_carpeta")
print("folder_id: %s" % folder_id)
file_id = gadrive.create_file("secret.txt", "secreto.txt", folder_id)
print("file_id: %s" % file_id)
files = gadrive.service.files().get(fileId=file_id, fields="parents").execute()
print("files: %s" % files)
"""