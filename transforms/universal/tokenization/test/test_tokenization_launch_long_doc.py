import os

from data_processing.test_support.ray import AbstractTransformLauncherTest
from tokenization_transform import TokenizationTransformConfiguration


tkn_params = {
        "tkn_tokenizer": "hf-internal-testing/llama-tokenizer",
        "tkn_doc_id_column":"document_id",
        "tkn_doc_content_column":"contents",
        "tkn_text_lang": "en",
        "tkn_chunk_size":20_000,
        }
class TestRayTokenizationTransform(AbstractTransformLauncherTest):
    """
    Extends the super-class to define the test data for the tests defined there.
    The name of this class MUST begin with the word Test so that pytest recognizes it as a test class.
    """

    def get_test_transform_fixtures(self) -> list[tuple]:
        basedir = "../test-data"
        basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), basedir))
        fixtures = [(TokenizationTransformConfiguration(), tkn_params, basedir + "/ds02/input", basedir + "/ds02/expected")]
        return fixtures
