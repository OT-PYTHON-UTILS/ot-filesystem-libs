import logging
import yaml

class getYamlLoader:
        
    def _loadYaml(self,yaml_file_path):
        
        try: 
            load_file = open(yaml_file_path)
            parse_yaml = yaml.load(load_file, Loader=yaml.FullLoader)
            logging.info(f"Loaded conf file succesfully.")
            return parse_yaml
        except FileNotFoundError:
            logging.error(f"Unable to find conf file < {yaml_file_path} > Please mention correct property file path.")
            exit()

        return None