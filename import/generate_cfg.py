import os
import configparser

def generate_import_cfg():
    if not os.path.exists("import.cfg"):
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'wow_path': '',
                             'auctionator_path': ''}
        
        config['scan'] = {'prompt_timeout': '120',
                          'prompt_delay': '3600',
                          'wow_username': '',
                          'wow_password': ''}
        
        config['import'] = {}
        
        with open('import.cfg','w') as configfile:
            config.write(configfile)
            return True

if __name__ == "__main__":
    generate_import_cfg()
        