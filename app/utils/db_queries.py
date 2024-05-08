"""Sentencias de Consulta SQL para la base de datos"""
BPM_LOGIN_USER_QUERY = """SELECT DISTINCT 
                            urm_asig.ID_DEPARTAMENTO,
                            dep.ID_USUARIO,
                            usr.CORREO,
                            usr.CEDULA,
                            IFNULL(usr.CARGO, " ") AS CARGO_EMP,
                            usr.ID_USUARIO AS ID_USUARIO_EMP,
                            usr.NOMBRES,
                            usr.APELLIDOS,
                            CONCAT(usr.NOMBRES, " ", usr.APELLIDOS ) as NOMBRECOMPLETO_EMP,
                            dep.DESCRIPCION AS NOMBREDIRECCION,
                            (SELECT CONCAT(nombres, " ", apellidos) from ft_usuarios WHERE ID_USUARIO = dep.ID_USUARIO) AS NOMBRECOMPLETO,
                            (SELECT IFNULL(CARGO, "SIN CARGO") from ft_usuarios WHERE ID_USUARIO = dep.ID_USUARIO) AS CARGO,
                            dep.TELEFONO,
                            dep.EXTENSIONES,
                            dep.CORREO_DEP,
                            OBTENER_PRIMER_NOMBRE_PRIMER_APELLIDO(dep.ID_USUARIO) AS NOMBRECORTO_DIR,
                            OBTENER_PRIMER_NOMBRE_PRIMER_APELLIDO(urm_asig.ID_USUARIO) AS NOMBRECORTO_USUARIO
                            FROM urm_asignacion urm_asig
                            INNER JOIN ft_departamento dep
                            ON urm_asig.ID_DEPARTAMENTO = dep.ID_DEPARTAMENTO
                            INNER JOIN ft_usuarios usr
                            ON urm_asig.ID_USUARIO = usr.ID_USUARIO
                            WHERE urm_asig.ID_USUARIO = '{user}'
                            {havePass}AND usr.CLAVE = '{password}'
                            AND urm_asig.ESTADO = "A"
                            AND dep.ESTADO = "A" 
                            AND dep.ID_TIPO = "D"
                            -- ORDER BY urm_asig.ID_ASIGNACION DESC
                            LIMIT 1;"""