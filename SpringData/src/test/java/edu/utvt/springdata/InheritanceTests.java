package edu.utvt.springdata;

import edu.utvt.springdata.data.entities.Alumno;
import edu.utvt.springdata.data.entities.Administrativo;
import edu.utvt.springdata.data.repositories.AdministrativoRespository;
import edu.utvt.springdata.data.repositories.AlumnoRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

@SpringBootTest
public class InheritanceTests {

    @Autowired
    private AlumnoRepository alumnoRepository;

    @Autowired
    private AdministrativoRespository administrativoRespository;

    @Test
    void testSaveAlumno() throws ParseException {
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
        Date fechaNacimiento = sdf.parse("15/03/2004");

        Alumno alumno = new Alumno();
        alumno.setNombre("Carlos");
        alumno.setApellidos("Ortega");
        alumno.setEmail("ortega@gmail.com");
        alumno.setFechaNacimiento(fechaNacimiento);
        alumnoRepository.save(alumno);
    }

    @Test
    void testSaveAdministrativo() throws ParseException {
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
        Date fechaNacimiento = sdf.parse("20/03/2025");

        Administrativo administrativo = new Administrativo();
        administrativo.setNombre("Admin");
        administrativo.setApellidos("Admin");
        administrativo.setEmail("admin@gmail.com");
        administrativo.setFechaNacimiento(fechaNacimiento);
        administrativo.setSalario(4000.0);
        administrativoRespository.save(administrativo);
    }
}