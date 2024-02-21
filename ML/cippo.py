from typing import Optional

from google.api_core.client_options import ClientOptions
from google.cloud import documentai  # type: ignore

# TODO(developer): Uncomment these variables before running the sample.
project_id = "412996116194"
location = "us"  # Format is "us" or "eu"
processor_id = "66ecef3533517e2f" # Create processor before running sample
file_path = "/Users/sergiovillani/Downloads/x.pdf"
mime_type = "pdf" # Refer to https://cloud.google.com/document-ai/docs/file-types for supported file types
field_mask = "text"  # Optional. The fields to return in the Document object.

# processor_version_id = "YOUR_PROCESSOR_VERSION_ID" # Optional. Processor version to use

"""
process_document_sample(
  project_id="412996116194",
  location="us",
  processor_id="66ecef3533517e2f",
  file_path="/Users/sergiovillani/Downloads/1010733_BPO_REDACTED.pdf"
)

"""

def process_document_sample(
    project_id: str,
    location: str,
    processor_id: str,
    file_path: str,
    mime_type: str,
    field_mask: Optional[str] = None,
    processor_version_id: Optional[str] = None,
) -> None:
    # You must set the `api_endpoint` if you use a location other than "us".
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")

    client = documentai.DocumentProcessorServiceClient(client_options=opts)

    if processor_version_id:
        # The full resource name of the processor version, e.g.:
        # `projects/{project_id}/locations/{location}/processors/{processor_id}/processorVersions/{processor_version_id}`
        name = client.processor_version_path(
            project_id, location, processor_id, processor_version_id
        )
    else:
        # The full resource name of the processor, e.g.:
        # `projects/{project_id}/locations/{location}/processors/{processor_id}`
        name = client.processor_path(project_id, location, processor_id)

    # Read the file into memory
    with open(file_path, "rb") as image:
        image_content = image.read()

    # Load binary data
    raw_document = documentai.RawDocument(content=image_content, mime_type=mime_type)

    # For more information: https://cloud.google.com/document-ai/docs/reference/rest/v1/ProcessOptions
    # Optional: Additional configurations for processing.
    process_options = documentai.ProcessOptions(
        # Process only specific pages
        individual_page_selector=documentai.ProcessOptions.IndividualPageSelector(
            pages=[1]
        )
    )

    # Configure the process request
    request = documentai.ProcessRequest(
        name=name,
        raw_document=raw_document,
        field_mask=field_mask,
        process_options=process_options,
    )

    result = client.process_document(request=request)

    # For a full list of `Document` object attributes, reference this page:
    # https://cloud.google.com/document-ai/docs/reference/rest/v1/Document
    document = result.document

    # Read the text recognition output from the processor
    print("The document contains the following text:")
    print(document.text)










