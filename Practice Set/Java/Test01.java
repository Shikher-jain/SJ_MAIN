import java.util.Scanner;

public class Test01 {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter a = ");
        int a=sc.nextInt();
        System.out.println("Enter b = ");
        int b=sc.nextInt();
        System.out.println("Enter c = ");
        int c=sc.nextInt();

        System.out.print("a+b+c= ");
        System.out.print(a+b+c);
    }
}