from decouple import config
from storages.backends.s3boto3 import S3Boto3Storage


class BaseR2Storage(S3Boto3Storage):
    # Keep object URLs stable (no expiring query-string signatures).
    default_acl = "public-read"
    querystring_auth = False
    bucket_name = config("AWS_STORAGE_BUCKET_NAME")
    endpoint_url = config("AWS_S3_ENDPOINT_URL")
    region_name = config("AWS_S3_REGION_NAME", default="auto")
    addressing_style = config("AWS_S3_ADDRESSING_STYLE", default="virtual")


class StaticFilesStorage(BaseR2Storage):
    location = "static"
    file_overwrite = True


class MediaFilesStorage(BaseR2Storage):
    location = "media"
    file_overwrite = False