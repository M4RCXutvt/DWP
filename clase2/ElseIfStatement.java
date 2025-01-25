package org.example.clase2;

public class ElseIfStatement {
    public static void main(String[] args) {
        int age = 16;
        if (age<=12)
            System.out.println("eres un niño");
        else if (age <17)
            System.out.println("eres adolecente");
        else if ( age < 35)
            System.out.println("eres un adulto joven");
        else
            System.out.println("eres adulto");
    }
}
