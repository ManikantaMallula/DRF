from logging import *
logformat='{lineno} *** {name} *** {time} *** {message}'

basicConfig(filename="logg6.log",level=DEBUG,filemode='w',style='{',format=logformat)
log=getLogger("happy")
log.debug("this is debug")
log.info("this is info")
log.warning("this is warning")
log.error("this is error")
log.critical("this is critical")