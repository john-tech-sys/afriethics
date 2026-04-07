# helpers/cloudflare/storages.py
from storages.backends.s3boto3 import S3Boto3Storage
from decouple import config

class StaticFilesStorage(S3Boto3Storage):
    location = "static"
    default_acl = "public-read"
    file_overwrite = True
    bucket_name = config("AWS_STORAGE_BUCKET_NAME")
    custom_domain = config("AWS_S3_ENDPOINT_URL")

class MediaFilesStorage(S3Boto3Storage):
    location = "media"
    default_acl = "public-read"
    file_overwrite = False
    bucket_name = config("AWS_STORAGE_BUCKET_NAME")
    custom_domain = config("AWS_S3_ENDPOINT_URL")