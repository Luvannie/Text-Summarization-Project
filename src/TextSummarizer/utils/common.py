import os
import yaml
from TextSummarizer.logging import logger
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from box import ConfigBox
from typing import Any
from pathlib import Path

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> config_box:
    """
    reads yaml file and returns
    Args:
        path_to _yaml (str): path like input
    Raises: 
        valueError: if yaml file is empty
        e: empty file
    
    Returns:
        config_box: configbox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded succesfully")
            return ConfigBox(content)
    except BoxValueError:
            raise ValueError("yaml file is empty")
    except Exception as e:
         raise e 
    
@ensure_annotations
def create_directories(path_to_dir: list,verbose = True):
     """
     Args:
        path_to_dir (list): list of path of directories
        ignore_log(bool, optional): ignore if multiple dirs is to be created. Default to False
     """    
     for path in path_to_dir:
          os.makedirs(path,exist_ok=True)
          if verbose:
               logger.info(f"create directory as : {path}")


@ensure_annotations
def get_size(path: Path)-> str:
     """get size of file in KB
     Args:
        path(Path): path of the file
    Returns:
        str:size in KB
     """
     size_in_KB = round(os.path.getsize(path)/1024)
     return f"~{size_in_KB} KB"