import java.util.Scanner;

public class VIPCafe {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] priorities = new int[n];
        for (int i = 0; i < n; i++) {
            priorities[i] = scanner.nextInt();
        }
        int k = scanner.nextInt();
        int served = 0;
        int index = k - 1;
        while (true) {
            int max = 0;
            int maxIndex = 0;
            for (int i = 0; i < n; i++) {
                if (priorities[i] > max) {
                    max = priorities[i];
                    maxIndex = i;
                }
            }
            served++;
            if (maxIndex == index) {
                break;
            }
            for (int i = 0; i < maxIndex; i++) {
                priorities[i]++;
            }
            for (int i = maxIndex; i < n - 1; i++) {
                priorities[i] = priorities[i + 1];
            }
            n--;
            if (index > maxIndex) {
                index--;
            }
        }
        System.out.println(served);
        scanner.close();
    }
}