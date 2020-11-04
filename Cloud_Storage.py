import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token

    def upload_files(self, file_from, file_to):
        dbx= dropbox.Dropbox(self.access_token)
        f=open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token='jGuqNmw-mgsAAAAAAAAAAXdHAbHv-teuDyVhosZghsFXae6zsk8gIp96du8e2UKh'
    transferData=TransferData(access_token)

    file_from=input("Enter the file path to transfer: ")
    file_to=input("Enter the full path to upload to dropbox: ")

    transferData.upload_files(file_from, file_to)
    print("File has been moved!!!")

main()