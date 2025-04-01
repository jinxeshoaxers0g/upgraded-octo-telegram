import java.util.regex.*;

class PasswordStrength {
    public static void main(String[] args) {
        String password = "P@ssw0rd123";
        if (isStrong(password)) {
            System.out.println("✅ Strong password!");
        } else {
            System.out.println("❌ Weak password!");
        }
    }

    static boolean isStrong(String password) {
        String regex = "^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d)(?=.*[@#$%^&+=]).{8,}$";
        return Pattern.matches(regex, password);
    }
}
