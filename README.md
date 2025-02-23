### Random scripts
 Recently interviewed for a role, but I was unable to solve 2 out of 4 questions within the interview timeframe. After the interview, I reviewed both questions.
- [x] For the **q1_s3_bucket.jpeg** challenge, I encountered credentials & header auth errors. After the interview, I realized that I needed to add the line `config=Config(signature_version=UNSIGNED)` to access the public bucket anonymously.
- [x] For the **q2_bash_logs.jpeg** challenge, I had issues capturing logs with value `fwd=MASKED`. I was only able to print out the first condition
- [x] I used **x1_delete_git_in_folder.sh** script to delete all Git files in subdirectories, excluding those in the root folder.# scripts
