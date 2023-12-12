# queries.py

from graphene import ObjectType, String
from icecream import ic


class Query(ObjectType):
    upload_file_content = String(content=String())

    def resolve_upload_file_content(self, info, content):
        # Handle the uploaded file content using icecream
        ic(content)

        # Return success
        return "success"
