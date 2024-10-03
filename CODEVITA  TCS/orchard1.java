import java.util.Scanner;

public class orchard1 {
    public static int countValidCombination(String row) {
        int n = row.length();
        int count = 0;
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (row.charAt(i) != row.charAt(j) && row.charAt(j) != row.charAt(k)) {
                        count++;
                    }
                }
            }
        }
        return count;
    }

    public static String winner(String row1, String row2) {
        if (!row1.matches("[ML]*") || !row2.matches("[ML]*")) {
            return "Invalid input";
        }
        int count1 = countValidCombination(row1);
        int count2 = countValidCombination(row2);
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

// //MMLMLLM

// // LMLLLMLM

