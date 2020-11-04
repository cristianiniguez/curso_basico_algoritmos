package recursividad;

public class StringReverse {
  public static String reverseString(String str) {
    if (str.isEmpty()) {
      return str;
    } else {
      return reverseString(str.substring(1)) + str.charAt(0);
    }
  }

  public static void main(String[] args) {
    String result = StringReverse.reverseString("Algorithms are love");
    System.out.println(result);
  }
}
