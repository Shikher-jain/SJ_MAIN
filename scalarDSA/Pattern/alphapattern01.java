public class alphapattern01{
    public static void main(String[] args) {

        int n=6;
        for(int i=1 ; i<=n ; i++){
            char value='A';
            for (int j=1 ; j<=i ; j++){
                System.out.print(value+" ");
                value = (char)(value + 1);
            }
            System.out.println();
        }
    }
}