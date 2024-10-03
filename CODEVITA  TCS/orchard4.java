import java.util.Scanner;

public class orchard4 {
    public static String winner(String row1, String row2) {
        if (!row1.matches("[ML]*") || !row2.matches("[ML]*")) {
            return "Invalid input";
        }
        int n1 = row1.length();
        int n2 = row2.length();
        int[] dp1 = new int[n1];
        int[] dp2 = new int[n2];
        dp1[0] = 1;
        dp2[0] = 1;
        dp1[1] = 2;
        dp2[1] = 2;
        for (int i = 2; i < n1; i++) {
            if (row1.charAt(i) != row1.charAt(i - 1)) {
                dp1[i] = dp1[i - 1] + dp1[i - 2];
            } else {
                dp1[i] = dp1[i - 1];
            }
        }
        for (int i = 2; i < n2; i++) {
            if (row2.charAt(i) != row2.charAt(i - 1)) {
                dp2[i] = dp2[i - 1] + dp2[i - 2];
            } else {
                dp2[i] = dp2[i - 1];
            }
        }
        int count1 = 0;
        int count2 = 0;
        for (int i = 0; i < n1 - 2; i++) {
            count1 += dp1[i] * (n1 - i - 2);
        }
        for (int i = 0; i < n2 - 2; i++) {
            count2 += dp2[i] * (n2 - i - 2);
        }
        if (count1 > count2) {
            return "Ashok";
        } else if (count2 > count1) {
            return "Anand";
        } else {
            return "Draw";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String row1 = scanner.nextLine();
        String row2 = scanner.nextLine();
        String result = winner(row1, row2);
        System.out.println(result);
        scanner.close();
    }
}
