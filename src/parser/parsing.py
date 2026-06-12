from ..models.zone_class import Zone
from ..models.connection_class import Connection
class Pars_exception(Exception):
    pass
class Read_input_file:
    def __init__(self):
        self.nb_drones = 0
        self.zones = {}
        self.connections = []
        self.star_hub= None
        self.end_hub = None

    def read_file(self,config_file: str)->dict:
        
        try:
            with open(config_file, 'r') as file:
                lines = file.readlines()
                
        except FileNotFoundError as e:
            return f"{e}"

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
                         raise Pars_exception("number of drones  must be a number")
                    self.nb_drones = value
                if key in ("start_hub", "hub", "end_hub"):
                    part_value = value.strip().split(" ",3)
                    if len(part_value) == 3:
                        name,x,y = part_value
                        meta = None


                    elif len(part_value) == 4:
                        name,x,y,meta = part_value


                    if  not isinstance(name,str):
                        raise Pars_exception("name not  a string")
                    try:
                        x = int(x)
                        y= int(y)
                        if x < 0 or y < 0:
                            raise Pars_exception("x or y is not a valid integer")
                    except  ValueError:
                        raise Pars_exception("x or y is not a valid integer")
        
                    if len(part_value) == 4:
                        meta = meta.strip()

                        if not meta.startswith("["):
                                raise Pars_exception("metadata  must start with '['")
                        
                        if not meta.endswith("]") :
                            raise Pars_exception("metadata  must end with ']'")
                        
                        meta_content = meta[1:-1].strip()
                        met_zone = meta_content.strip().split(" ")

                        dict_meta ={}
                        for element in met_zone:
                            element = element.strip()
                            if "=" not in element:
                                raise Pars_exception("meta must have '='")
                        
                        
                            meta_key,meta_value = element.split("=",1)
                            meta_key = meta_key.strip()
                            meta_value = meta_value.strip()
                            if meta_key not in ("zone","color","max_drones"):
                                raise Pars_exception("metadata should  be a zone ,color,max_drones")
                            
                            if meta_key == "zone":
                                if meta_value not in ("normal","blocked","restricted","priority"):
                                    raise Pars_exception("metadata zone must be 'normal,blocked,restricted,priority'")
                        
                            if meta_key == "max_drones":
                                try:
                                    meta_value = int(meta_value)
                                    if  meta_value < 0:
                                        raise Pars_exception("metadata max_drones must be a number")
                                except:
                                    raise Pars_exception("metadata max_drones must be a number")
                            
                            dict_meta[meta_key]=meta_value
                        meta=dict_meta
                        
                    zone = Zone(name,x,y,meta)
                    # print(f"zone:{zone.name,zone.x,zone.y,zone.metadata}")
                    self.zones[zone.name]= zone  
                if key == "start_hub":
                     self.star_hub = zone.name
                if key == "end_hub":
                     self.end_hub = zone.name

                if key == "connection":

                    part_value =  value.strip().split(" ",1);
                    
                    if len(part_value) == 1:
                        part_con_name = part_value[0].split("-",1);
                        name1,name2 = part_con_name
                        meta_con = None
                    
                    

                    elif len(part_value) == 2:
                        part_con_name = part_value[0].split("-",1)
                        name1,name2 = part_con_name
                        meta_con = part_value[-1]

                        if not meta_con.startswith("["):
                                raise Pars_exception("metadata  must start with '['")
                        
                        if not meta_con.endswith("]") :
                                raise Pars_exception("metadata  must end with ']'")

                        if "=" not in meta_content:
                            raise Pars_exception("meta must have '='")
                        
                        meta_con = meta_con[1:-1].strip()
                        
                        met_con_check = meta_con.strip().split(" ",1)
                       
                        if len(met_con_check) != 1:
                             raise Pars_exception("metadata in connection should be  just a max_link_capacity")

                        meta_con_key,meta_con_value = met_con_check[0].split("=",1)

                        if meta_con_key.strip() != "max_link_capacity":
                            raise Pars_exception("metadata in connection should be  just a max_link_capacity")

                       
                        meta_con = {meta_con_key.strip(): meta_con_value.strip()}

                    if not isinstance(name1,str) or not isinstance(name2,str):
                            raise Pars_exception("connection not correct")  
                    
                    connection = Connection(name1,name2,meta_con)

                    # print(f" connection:{connection.name1,connection.name2,connection.metadata}")
                    

                    for element in self.connections:
                        if connection.name1 == element.name1 and connection.name2 == element.name2:
                              raise Pars_exception("connectios is duplicate",connection.name1)
                        if connection.name1 == element.name2 and connection.name2 == element.name1:
                              raise Pars_exception("connectios is duplicate",connection.name1)
                    self.connections.append(connection)
                        
                            

            for connection in self.connections:
                    if connection.name1 not in self.zones:
                       raise Pars_exception("connection is not in zones ",connection.name1)
                    if connection.name2 not in self.zones:
                       raise Pars_exception("connection is not in zones ",connection.name2)
           
             
            return [self.nb_drones, self.zones,self.connections,self.star_hub,self.end_hub]
        except Pars_exception as e:
            return f"{e}"

class Parser:
     pass