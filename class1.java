import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class class1 {
    private double balance = 0.0;
    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new class1().createAndShowGUI());
    }

    private void createAndShowGUI() {
        JFrame frame = new JFrame("Simple Bank Application");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.setLayout(new GridLayout(5, 2));

        JLabel balanceLabel = new JLabel("Current Balance: $0.00");
        JTextField amountField = new JTextField();
        JButton depositButton = new JButton("Deposit");
        JButton withdrawButton = new JButton("Withdraw");
        JButton exitButton = new JButton("Exit");

        depositButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    double amount = Double.parseDouble(amountField.getText());
                    if (amount > 0) {
                        balance += amount;
                        balanceLabel.setText(String.format("Current Balance: $%.2f", balance));
                        amountField.setText("");
                    } else {
                        JOptionPane.showMessageDialog(frame, "Please enter a positive amount.", "Error", JOptionPane.ERROR_MESSAGE);
                    }
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(frame, "Invalid amount. Please enter a number.", "Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        withdrawButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    double amount = Double.parseDouble(amountField.getText());
                    if (amount > 0 && amount <= balance) {
                        balance -= amount;
                        balanceLabel.setText(String.format("Current Balance: $%.2f", balance));
                        amountField.setText("");
                    } else {
                        JOptionPane.showMessageDialog(frame, "Invalid amount. Check your balance or enter a positive amount.", "Error", JOptionPane.ERROR_MESSAGE);
                    }
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(frame, "Invalid amount. Please enter a number.", "Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        exitButton.addActionListener(e -> System.exit(0));

        frame.add(balanceLabel);
        frame.add(new JLabel("Amount:"));
        frame.add(amountField);
        frame.add(depositButton);
        frame.add(withdrawButton);
        frame.add(exitButton);

        frame.setVisible(true);
    }
}
