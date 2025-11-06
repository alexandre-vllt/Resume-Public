# My projects 

This repository showcases several projects I completed during my double degree between CentraleSupélec (General Engineering) and EPFL (Bachelor in Mechanical Engineering and Master in Data Science). Each project reflects my growing expertise in engineering, data analysis, and computational modeling, combining technical rigor with practical problem-solving.

## Project ML : Cardiovascular Disease Prediction only with numpy 

This project focuses on predicting cardiovascular disease (CVD) using the Behavioral Risk Factor Surveillance System (BRFSS) dataset of over 400,000 individuals. Following extensive data cleaning and preprocessing, we implemented and compared several logistic regression models, including Ridge and class-weighted versions to handle class imbalance.

All computations were done exclusively with NumPy, without relying on external machine learning libraries. The final class-weighted logistic regression achieved an F1-score of 0.43 and accuracy of 87.5%, demonstrating effective detection of positive CVD cases and strong skills in low-level numerical programming, data analysis, and model optimization.


## Project 1 : A 2D platformer built with Python

This project is a side-scrolling 2D platformer inspired by classic games like Super Mario. Built with Python and Pygame, it features a playable character that moves, jumps, and explores levels filled with obstacles and enemies.

The game includes gravity and collision mechanics, sprite animations, and level progression. The code is organized around object-oriented design, making it modular and easy to extend.

This game was developed during Coding Week at CentraleSupélec, a one-week event dedicated to creating a group programming project from scratch.


## Project 2 : Stock Market Nonlinear Dynamics Modeling

This project explores the nonlinear evolution of stock market prices through a discrete-time dynamical system inspired by Bischi & Valori’s model. Using Python simulations, we developed and analyzed a model that couples the interaction between price (P) and investor savings (S) while integrating nonlinear terms and random external events to better mimic real market behaviors. The study includes stability analysis, simulation of equilibrium points, and the creation of a hybrid automaton to capture sudden market shifts. This work demonstrates how nonlinearity and randomness can explain the complex oscillations and volatility observed in real financial markets.

## Project 3 : High-Performance Task Scheduling Optimization (ST7 – ANEO Project)

This project focuses on optimizing the scheduling of task graphs for high-performance computing (HPC) environments using the HLFET (Highest Level First with Estimated Times) heuristic. Implemented in Python, the algorithm was designed to minimize the total execution time (makespan) of complex dependency graphs while maintaining computational efficiency.

After a theoretical study and problem formalization, the algorithm was implemented locally and then deployed on AWS Lambda to evaluate scalability and performance on large-scale DAGs (up to 100,000 tasks). The results showed that HLFET consistently outperforms greedy approaches in execution efficiency, achieving near-linear scalability in cloud environments.

## Project 4 : Nonparametric and Linear Regression Analysis

This project explores statistical modeling and regression techniques using Python, focusing on both linear and nonparametric regression methods. The work aims to compare the predictive performance, interpretability, and flexibility of models when applied to real or simulated datasets.

The Linear Regression module introduces classical parametric estimation, exploring coefficient significance and residual analysis. The Nonparametric Regression study (kernel and local polynomial approaches) highlights how relaxing linearity assumptions allows for more adaptable models that capture complex relationships in data.

## Project 5 Mechanical Design Project : Automatic Carrot Peeler

This project, completed as part of the Mechanical Construction II course at EPFL, involved the design and development of a fully mechanical carrot-peeling machine. The goal was to create a reliable, ergonomic, and safe device that minimizes the effort required from the user while optimizing peeling speed and efficiency.

## Project 6 : Billiard Motion Analysis System 

This project focuses on the automated analysis of a French billiards game using a combination of C, MATLAB, and LabVIEW. The system processes a sequence of images to detect, track, and analyze the trajectories of billiard balls, identifying rebounds, collisions, and determining whether the player scored.

The C program handles low-level image processing — extracting pixel data and identifying ball positions based on color segmentation. MATLAB scripts perform trajectory reconstruction, interpolation of missing data, and visualization of ball paths and collision points. Finally, the LabVIEW interface orchestrates the workflow, calling the C and MATLAB components while providing a user-friendly visualization and error-handling environment.

This project demonstrates strong skills in multi-language integration, image processing, signal analysis, and system automation, showcasing the ability to combine embedded programming and graphical environments to solve a real-world physics-based problem.

## Project 7 : Autonomous Vehicle 

This project involves the design of an autonomous vehicle capable of line tracking and obstacle detection using infrared sensors, ultrasonic modules, and a camera controlled via Raspberry Pi and Arduino. The robot follows a path, avoids obstacles, and returns automatically to its base after completing its mission.

It showcases skills in embedded systems, robotics, and real-time control, combining sensor integration and autonomous navigation algorithms within a compact and efficient robotic platform.
