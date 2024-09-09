import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Maain_1 {
    public static void main(String[] args) {
        String regex = "w+s";
        String str = "fee fi fo fum";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(str);

        while (matcher.find()) {
            System.out.println(matcher.group());
        }
    }
}