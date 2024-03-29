import os
import sys

from data_processing.ray import TransformLauncher
from data_processing.utils import ParamsUtils
from tokenization_transform import TokenizationTransformConfiguration


# create parameters
input_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "test-data","ds02", "input"))
output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "output","ds02"))
local_conf = {
    "input_folder": input_folder,
    "output_folder": output_folder,
}
worker_options = {"num_cpus": 0.8}
code_location = {"github": "github", "commit_hash": "12345", "path": "path"}
params = {
    "run_locally": True,
    "max_files": -1,
    "local_config": ParamsUtils.convert_to_ast(local_conf),
    "worker_options": ParamsUtils.convert_to_ast(worker_options),
    "num_workers": 5,
    "checkpointing": False,
    "pipeline_id": "pipeline_id",
    "job_id": "job_id",
    "creation_delay": 0,
    "code_location": ParamsUtils.convert_to_ast(code_location),
    "tkn_tokenizer": "hf-internal-testing/llama-tokenizer",
    "tkn_chunk_size":20_000,
}
if __name__ == "__main__":
    """
    This shows the impact of `tkn_chunk_size` in tokenizing a long document (~16.8 million characters).
    Tokenizing the whole document in a single shot (i.e., tkn_chunk_size=0) can take much longer time 
    than splitting it into chunks of ~20_000 characters each.
    """

    sys.argv = ParamsUtils.dict_to_req(d=params)
    # create launcher
    launcher = TransformLauncher(transform_runtime_config=TokenizationTransformConfiguration())
    # Launch the ray actor(s) to process the input
    launcher.launch()
