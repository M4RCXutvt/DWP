package edu.utvt.springdata;

import edu.utvt.springdata.data.entities.Player;
import edu.utvt.springdata.data.repositories.PlayerRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;

import java.util.List;

@SpringBootTest
public class JPAQueryMethods {

    @Autowired
    private PlayerRepository playerRepository;

    @Test
    void findByFullName(){
        String fullName = "Harrison Ingram";
        playerRepository.findByFullName(fullName).forEach(System.out::println);
    }

    @Test
    void findByFullNameContaining(){
        String name = "Harrison";
        this.playerRepository.findByFullNameContaining(name).forEach(System.out::println);
    }

    @Test
    void findByTeamAndAge(){
        String team = "Uta";
        Integer age = 21;

        this.playerRepository.findByTeamAndAge(team, age).forEach(System.out::println);
    }

    @Test
    void findByTeamAndPeagable(){
        Pageable peagable = PageRequest.of(0, 10);
        Page<Player> page = this.playerRepository.findByTeam("Uta", peagable);
        System.out.println(page);

    }

}
