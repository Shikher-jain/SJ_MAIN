// package SJ_MAIN.scalarDSA;

import java.util.Scanner;

public class MathDemo{
    
    public static double circleArea(int r){
        return  (double) (Math.PI * r * r) ;
    }

    public static double RandomNO() {
        for(int i = 0;1<=5;i++){
            System.out.println( Math.random());
        }
    }
    public static void main(String[] args) {

        // Scanner sc =new Scanner(System.in);

        // int r = sc.nextInt();
        int r=5;
        System.out.println("Math Module");
        System.out.println(String.format("%.3f",circleArea(r)));
    
        System.out.println(Math.PI);
        RandomNO();


    }
}
