import java.util.Scanner;

public class Main02 {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("Execptions: ");
        System.out.println("Enter No. 1:");
        int n1 = scn.nextInt();
        System.out.println("Enter No. 2:");
        int n2 = scn.nextInt();

        try {
            int result = divide(n1, n2);
            System.out.println("Result = " + result);
        } catch (Exception e) {
            System.out.println(e);
            // System.out.println(e.getLocalizedMessage());
            System.out.println(e.getMessage());
        }
    }

    static int divide(int a, int b) {
        return a / b;
    }
}