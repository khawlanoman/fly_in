
class Read_input_file:
    def __init__(self):
        self.nb_drones= 0;
        self.start_hub={},
        self.end_hub={},
        self.hub={},
        self.connection= {}
    def read_file(self,config_file: str)->dict:
        try:
            with open(config_file, 'r') as file:
                lines = file.readlines()
                print(lines)
        except:
            print("error");
class Parser:
    pass