# Faulu-Hub
ELEARNING WEBAPP MADE WITH BOOTSRTAP 4 ON FRONTEND AND PYTHON DJANGO ON BACKEND.

# Features
EXAMINATION SYSTEM <br>
STUDY NOTES SYSTEM <br>
BLOG <br>
BOOKS SYSTEM <br>
VIDEO LEARNING SYSTEM <br>
ONLINE SUPPORT <br>
DISCUSSION FORUM <br>
CONTACT US SYSTEM <br>
CLEAN UI<br>

To run the project, headup to
# settings.py and edit 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'<br>
DEFAULT_FROM_EMAIL = 'EMAIL HERE EXAMPLE luqman@gmail.com'<br>
EMAIL_HOST = 'EMAIL HOST HERE EXAMPLE mail.gmail.com'<br>
EMAIL_HOST_USER = 'EMAIL HOST USER'<br>
EMAIL_HOST_PASSWORD = 'YOUR PASSWORD'<br>
EMAIL_PORT = 587<br>
EMAIL_USE_TLS = True<br>
FAIL_SILENTLY = False<br>

<br>
# AWS MEDIA FILE STORAGE
AWS_ACCESS_KEY_ID = 'AWS KEY ID HERE'<br>
AWS_SECRET_ACCESS_KEY = 'AWS SECRET KEY'<br>
AWS_STORAGE_BUCKET_NAME = 'AWS STORAGE NAME'<br>
# AWS_S3_REGION_NAME = 'us-east-'<br>
# AWS_S3_SIGNATURE_VERSION = 's3v4'<br>
AWS_S3_FILE_OVERWRITE = False<br>
AWS_DEFAULT_ACL = None<br>
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'<br>

# run pip install -r requirements.txt
# python manage.py runserver
