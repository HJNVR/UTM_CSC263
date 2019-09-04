% Assignment Document Class (for CSC263)
% Copyright 2013, David Liu
% Modified by Larry Zhang, 2016
% Note to students: while you need to have this file to compile the problem
% set files, you don't need to understand the contents of this file to be
% successful with LaTeX.

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{assignment}[11/27/13 Assignment Document Class]

\LoadClass{article}

\renewcommand{\normalsize}{\fontsize{10pt}{13pt}\selectfont}

% Default paper size letter
\usepackage[letterpaper, margin=1.25cm]{geometry}

% Import package
\usepackage{ut-csc}
\usepackage{enumerate}

% Length parameters
\setlength{\parindent}{0pt}
\setlength{\parskip}{\baselineskip/5}
\setlength{\smallskipamount}{5pt}
\setlength{\bigskipamount}{15pt}

% Remove page numbers
\pagenumbering{gobble}

% Title
\newcommand{\anum}[1]{\gdef\@anum{#1}}
\newcommand{\course}[1]{\gdef\@course{#1 }}
\newcommand{\total}[1]{\gdef\@total{#1} }
\newcommand{\duedate}[1]{\gdef\@duedate{#1}}
\newcommand{\filename}[1]{\gdef\@filename{#1}}
\newcommand{\prelimduedate}[1]{\gdef\@prelimduedate{#1}}

\renewcommand{\maketitle}{
	\centerline{\textbf{\huge{\@course -- Problem Set \@anum}}}
	\bigskip
	%\centerline{\large{\textbf{\@total} marks total}}
	%\vspace{15pt}
	%\centerline{\large{Due \@duedate}}
	%\vspace{10pt}
}

% The preamble
\newcommand{\makepreamble}{
\qquad \qquad \qquad Si Tong Liu(1004339628), Jing Huang(1003490705), Yifei Gao(1004152640)\vskip5pt
Remember to write your \textbf{full name} and \textbf{student number}
prominently on your submission.
To avoid suspicions of plagiarism: at the beginning of your submission,
\textbf{clearly state any resources (people, print, electronic) outside of
your group, the course notes, and the course staff, that you consulted}. 

Remember that you are required to submit your problem sets as both La\TeX
\texttt{.tex} source files and \texttt{.pdf} files. There is a 10\% penalty
on the assignment for failing to submit both the \texttt{.tex} and
\texttt{.pdf}.

\bigskip
\hrule
}

\newcommand{\prelim}{
	\section*{Preliminary: Not Marked}
	This question is an opportunity for you to check your understanding of
	the topics and practice writing formal solutions.
	This is a valuable \emph{learning opportunity} -- if you see that you're
	at a loss, get help quickly!
	
	
	\smallskip
}

\newcommand{\think}{
	\subsection*{Due {\@duedate}, 22:00; required files: {\@filename}}

	Answer each question completely, always justifying your claims and
	reasoning.  Your solution will be graded not only on correctness, but
	also on clarity.  Answers that are technically correct that are hard to
	understand will not receive full marks.  Mark values for each question
	are contained in the [square brackets].
	
	\textbf{You may work in groups of up to THREE to complete these questions.} 
	
	\smallskip
}


\newcommand{\program}{
	\section*{Programming Question}

	The best way to learn a data structure or an algorithm is to code it up.
	In each problem set, we will have a programming exercise for which you
	will be asked to write some code and submit it. You may also be asked to
	include a write-up about your code in the PDF/\TeX file that you submit.
	Make sure to \textbf{maintain your academic integrity} carefully, and
	protect your own work. The code you submit will be checked for
	plagiarism. It is much better to take the hit on a lower mark than
	risking much worse consequences by committing an academic offence.
	
	\smallskip
}

\AtBeginDocument{\maketitle \makepreamble}
