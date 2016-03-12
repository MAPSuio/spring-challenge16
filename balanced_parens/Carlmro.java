import java.util.Scanner;

public class Carlmro {

    public static boolean wellFormed(String expression){

        int counter = 0;
        char[] expressionArray = expression.toCharArray();

        for(char c: expressionArray){
            counter += (c == '(' ? 1 : -1);
            if(counter < 0)
                return false;
        }

        return counter == 0;
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int wellFormedExpressions = 0;

        while(scanner.hasNext()){
            if(wellFormed(scanner.next())){
                wellFormedExpressions += 1;
            }
        }

        System.out.println(wellFormedExpressions);
    }
}
