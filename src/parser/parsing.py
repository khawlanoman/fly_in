from ..models.zone_class import Zone
from ..models.connection_class import Connection
import sys
class Pars_exception(Exception):
    pass

class Read_input_file:
    def __init__(self):
        self.nb_drones = 0
        self.zones = {}
        self.connections = []
        self.star_hub= None
        self.end_hub = None

    def read_file(self,config_file: str)->list:
        
        try:
            with open(config_file, 'r') as file:
                lines = file.readlines()
                
        except FileNotFoundError as e:
            print( f"{e}")
            sys.exit(1)

        try:
            
            for l_line in lines:
                line = l_line.strip()
                if not line:
                    continue
                elif(line.startswith("#")):
                        continue
                
                key,value = line.split(":",1)

                if key == "nb_drones":
                    try:
                        value = int(value)
                    except:
                        raise Pars_exception(f"\nError:  nb_drones should be a integer\n")
                        # sys.exit(1)
                    self.nb_drones = int(value)
                # print(f"nb:{value}")
                if key in ("start_hub", "hub", "end_hub"):
                    part_value = value.strip().split(" ",3)
                    if len(part_value) == 3:
                        name,x,y = part_value
                        meta = None

                    elif len(part_value) == 4:
                        name,x,y,meta = part_value

                    if  not isinstance(name,str):
                        raise Pars_exception("\nERROR :name not  a string\n")
                    try:
                        x = int(x)
                        y= int(y)

                    except  ValueError:
                        raise Pars_exception("\nERROR :x or y is not a valid integer\n")

                    if len(part_value) == 4:
                        meta = meta.strip()

                        if not meta.startswith("["):
                                raise Pars_exception("\nERROR :metadata  must start with '['\n")

                        if not meta.endswith("]") :
                            raise Pars_exception("\nERROR :metadata  must end with ']'\n")
                        
                        meta_content = meta[1:-1].strip()
                        met_zone = meta_content.strip().split(" ")

                        dict_meta ={}
                        for element in met_zone:
                            element = element.strip()
                            if "=" not in element:
                                raise Pars_exception("\nERROR :meta must have '='\n")

                            meta_key,meta_value = element.split("=",1)
                            meta_key = meta_key.strip()
                            meta_value = meta_value.strip()
                            if meta_key not in ("zone","color","max_drones"):
                                raise Pars_exception("\nERROR :metadata should  be a zone ,color,max_drones\n")
                            
                            if meta_key == "zone":
                                if meta_value not in ("normal","blocked","restricted","priority"):
                                    raise Pars_exception("\nERROR :metadata zone must be 'normal,blocked,restricted,priority'\n")
                        
                            if meta_key == "max_drones":
                                try:
                                    meta_value = int(meta_value)
                                    if  meta_value < 0:
                                        raise Pars_exception("\nERROR :metadata max_drones must be a number\n")
                                except:
                                    raise Pars_exception("\nERROR :metadata max_drones must be a number\n")
                            
                            dict_meta[meta_key]=meta_value
                        meta=dict_meta
                        
                    zone = Zone(name,x,y,meta)

                    self.zones[zone.name]= zone
                if key == "start_hub":
                     self.star_hub = zone.name
                if key == "end_hub":
                     self.end_hub = zone.name

                if key == "connection":

                    part_value =  value.strip().split(" ",1);
                    # print("part",part_value)
                    if len(part_value) == 1:
                        part_con_name = part_value[0].split("-",1);
                        if len(part_con_name) == 2:
                            name1,name2 = part_con_name
                            meta_con = None
                        else:
                            raise Pars_exception("\nERROR :connection names  should be 2\n")

                    elif len(part_value) == 2:
                        part_con_name = part_value[0].split("-",1)
                        if len(part_con_name) == 2:
                            name1,name2 = part_con_name
                            meta_con = part_value[-1]
                        else:
                            # print("hi")
                            raise Pars_exception("\nERROR :connection names  should be 2\n")

                        if not meta_con.startswith("["):
                                raise Pars_exception("\nERROR :metadata  must start with '['\n")
                        
                        if not meta_con.endswith("]") :
                                raise Pars_exception("\nERROR :metadata  must end with ']'\n")

                        if "=" not in meta_content:
                            raise Pars_exception("\nERROR :meta must have '='\n")
                        
                        meta_con = meta_con[1:-1].strip()
                        
                        met_con_check = meta_con.strip().split(" ",1)
                       
                        if len(met_con_check) != 1:
                             raise Pars_exception("\nERROR :metadata in connection should be  just a max_link_capacity\n")

                        meta_con_key,meta_con_value = met_con_check[0].split("=",1)

                        if meta_con_key.strip() != "max_link_capacity":
                            raise Pars_exception("\nERROR :metadata in connection should be  just a max_link_capacity\n")

                       
                        meta_con = {meta_con_key.strip(): meta_con_value.strip()}

                    if not isinstance(name1,str) or not isinstance(name2,str):
                            raise Pars_exception("\nERROR :connection not correct\n")  
                    
                    connection = Connection(name1,name2,meta_con)

                    # print(f" connection:{connection.name1,connection.name2,connection.metadata}")
                    

                    for element in self.connections:
                        if connection.name1 == element.name1 and connection.name2 == element.name2:
                              raise Pars_exception("\nERROR :connectios is duplicate",connection.name1)
                        if connection.name1 == element.name2 and connection.name2 == element.name1:
                              raise Pars_exception("\nERROR :connectios is duplicate",connection.name1)
                    self.connections.append(connection)


            coor_zones = {}
            for connection in self.connections:
                    
                    if connection.name1 in self.zones.keys() and connection.name2 in self.zones.keys():
                        # print("in zones",name1)
                        # print("connection", connection.name1, connection.name2)
                        coor_zones[connection.name1] = (self.zones[connection.name1].x, self.zones[connection.name1].y)
                        coor_zones[connection.name2] = (self.zones[connection.name2].x, self.zones[connection.name2].y)
                        # print(coor_zones[connection.name1],coor_zones[connection.name2])
                    if connection.name1 not in self.zones.keys():
                       raise Pars_exception("\nconnection is not in zones ",connection.name1)
                    if connection.name2 not in self.zones.keys():
                       raise Pars_exception("\nconnection is not in zones ",connection.name2)

            # coor_values = coor_zones.values()
            # print(coor_zones)
            if len(coor_zones) != len(set( coor_zones.values())):
                raise Pars_exception("\nShould every zone have unique coordinates\n")

            return [self.nb_drones, self.zones,self.connections,self.star_hub,self.end_hub]
        except Pars_exception as e:
            print( f"{e}")
            sys.exit(1)
