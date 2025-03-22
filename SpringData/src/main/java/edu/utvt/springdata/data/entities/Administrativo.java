package edu.utvt.springdata.data.entities;

import jakarta.persistence.DiscriminatorValue;
import jakarta.persistence.Entity;
import lombok.*;

@Entity
@DiscriminatorValue(value = "2")
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
public class Administrativo extends Usuario {
    private Double salario;
}
