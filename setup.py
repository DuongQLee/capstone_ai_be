from google_drive_downloader import GoogleDriveDownloader as gdd

gdd.download_file_from_google_drive(file_id='1bRKFQLr7AWd1w3uK8ilqIxzeJEiFCb06',
                                    dest_path='./models/segmentation_model.pt',
                                    unzip=True)