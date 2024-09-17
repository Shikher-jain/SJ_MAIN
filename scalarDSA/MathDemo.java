// import java.util.Scanner;

public class MathDemo{
    
    public static double circleArea(int r){
        return  (double) (Math.PI * r * r) ;
    }

    public static void RandomNO() {
    
        for(int i = 0;i<=10;i++){
        System.out.print( (int)(Math.random()*10) + " ");   //0 -9
        }
        
    System.out.println();
        
    for(int i = 0;i<=10;i++){
            System.out.print( (int)(Math.random()*10)+1 + " ");   //1 -10
        }

    System.out.println();
        
    for(int i = 0;i<=20;i++){
            System.out.print( (int)(Math.random()*10)+11 + " ");   //11 -20
        }

    System.out.println();

    for(int i=0;i<=10;i++){
        System.out.print( (int)(Math.random()*10)+12/*yaha se 12+10-1 tak */ + " ");
    }

    System.out.println();

    for(int i=0;i<=10;i++){
        System.out.print( (int)(Math.random()*6)+12 + " "); //12 - 17 
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
