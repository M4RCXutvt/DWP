package org.example.clase2;
import java.util.Scanner;
public class ForLoop {
    public static void main(String[] args) {
    int loops= 0;
    Scanner sc= new Scanner(System.in);

        System.out.println("ingresa el numero de ciclos requeridos");
        loops= sc.nextInt();

        for ( int count = 1; count <= loops; count++) {
            System.out.println("numero actual de iteracion " + count);
        }

    }
}
