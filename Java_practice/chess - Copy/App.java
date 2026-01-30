import java.awt.BorderLayout;
import java.awt.GridLayout;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;

public class App {

    static String[][] board =  {
                        { "♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖" },
                        { "♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"},
                        {" "," "," "," "," "," "," "," "},
                        {" "," "," "," "," "," "," "," "},
                        {" "," "," "," "," "," "," "," "},
                        {" "," "," "," "," "," "," "," "},
                        { "♟︎", "♟︎", "♟︎", "♟︎", "♟︎", "♟︎", "♟︎", "♟︎"},
                        { "♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"}
                    };
    
    static void printBoard(String[][] board){
        boolean flipper = true;
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[i].length; j++){
                flipper = !flipper;
                if(board[i][j] != " "){
                    if(flipper){
                        System.out.print(" "+board[i][j]+" ");
                    }else{
                        System.out.print("#"+board[i][j]+"#");
                    }
                }else{
                    if(flipper){
                        System.out.print("   ");
                    }else{
                        System.out.print("###");
                    }
                }
            }
            flipper = !flipper;
            System.out.println();
        }
        
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Chess");

        frame.add(new JLabel("Chess w/o Rules", SwingConstants.CENTER), BorderLayout.NORTH);

        JPanel panel = new JPanel(new GridLayout(8,8));

        boolean flipper = true;
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[i].length; j++){
                JButton button = new JButton(String.valueOf(board[i][j]));
                panel.add(button);
            }
        }

        frame.add(panel, BorderLayout.CENTER);
        frame.setSize(500,500);
        frame.setVisible(true);

    }
}
