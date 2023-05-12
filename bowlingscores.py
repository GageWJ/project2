import csv
import tkinter as tk


class BowlingScore:
   def __init__(self):
       self.scores_file = 'bowling_scores.csv'


   def add_score(self, username, score_input):
       if not score_input:
           return
       try:
           score = int(score_input)
           if score <= 0 or score > 300:
               return "Score must be a positive number no greater than 300."
           else:
               with open(self.scores_file, 'a', newline='') as file:
                   writer = csv.writer(file)
                   if file.tell() == 0:
                       writer.writerow(["Username", "Score"])
                   writer.writerow([username, score])
               return "Score added successfully!"
       except ValueError:
           return "Invalid input. Score must be a positive integer."


   def get_stats(self, username):
       try:
           with open(self.scores_file, 'r') as file:
               reader = csv.reader(file)
               next(reader)
               scores = []
               for row in reader:
                   if row[0] == username:
                       scores.append(int(row[1]))
               if scores:
                   avg_score = sum(scores) / len(scores)
                   max_score = max(scores)
                   return f"Average score for {username}: {avg_score:.2f}\nHighest score for {username}: {max_score}"
               else:
                   return f"No scores found for {username}."
       except FileNotFoundError:
           return "There are no scores in the file yet."


class BowlingScoreGUI:
   def __init__(self):
       self.tracker = BowlingScore()
       self.root = tk.Tk()
       self.root.title("Bowling Score")


       username_label = tk.Label(self.root, text="Enter a username:")
       username_label.grid(row=0, column=0, padx=5, pady=5)
       self.username_box = tk.Entry(self.root)
       self.username_box.grid(row=0, column=1, padx=5, pady=5)


       input_label = tk.Label(self.root, text="Enter a score (0-300):")
       input_label.grid(row=1, column=0, padx=5, pady=5)
       self.input_box = tk.Entry(self.root)
       self.input_box.grid(row=1, column=1, padx=5, pady=5)


       add_button = tk.Button(self.root, text="Add Score", command=self.add_score)
       add_button.grid(row=2, column=0, padx=5, pady=5)
       stats_button = tk.Button(self.root, text="Get Stats", command=self.get_stats)
       stats_button.grid(row=2, column=1, padx=5, pady=5)


       self.result_label = tk.Label(self.root, text="")
       self.result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


       self.root.mainloop()


   def add_score(self):
       username = self.username_box.get()
       score_input = self.input_box.get()
       result = self.tracker.add_score(username, score_input)
       self.result_label.config(text=result)


   def get_stats(self):
       username = self.username_box.get()
       result = self.tracker.get_stats(username)
       self.result_label.config(text=result)


if __name__ == '__main__':
   BowlingScoreGUI()

