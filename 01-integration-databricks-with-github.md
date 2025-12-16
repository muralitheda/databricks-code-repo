# Steps for Integrating Databricks with GitHub

## 1. GitHub Account Creation and Initial Repository Setup

These steps will guide you through creating a GitHub account and setting up your very first code repository.

### 1. Account Setup

1.  **Create/Use a Gmail Account:** Ensure you have an active Gmail account or another preferred email for registration.
2.  **Go to GitHub:** Navigate to the official GitHub website: **`https://github.com/`**
3.  **Sign Up:** Click the **Sign up** button and choose the **"continue with Google"** option for a quick registration process.

### 2. Repository (Repo) Creation

This phase involves setting up your code repository and version control system.

1.  **Create a Repository:** Once logged in, click the **"New"** button (or the plus icon $\texttt{+}$) in the top-right corner to create a new repository. 
2.  **Repository Name:** Choose a descriptive and clear **Repository name** (e.g., `my-first-project`, `learning-markdown`).
3.  **Description:** Provide a brief **description** of what your repository will contain.
4.  **License:** It is highly recommended to select a **license**. Choose **Apache License 2.0** from the dropdown menu.

### 3. Adding and Committing Code

1.  **Add Your First Sample Code:** Create or upload your first file (e.g., a `README.md` or a simple `hello.py` file) directly through the GitHub interface or later via the command line.
2.  **Commit Your First Code:** **Commit** (save) the changes. A commit is essentially a snapshot of your code at a specific point in time. Add a clear commit message (e.g., "Initial commit: setting up project structure").

### 4. Local Setup

* **Clone Your Code:** To work on your code locally, you will **Clone** (download/pull) the repository to your computer using Git. This is the process for setting up the version control on your local machine.

***

## 2. Databricks Free Edition Setup (Forever Free)

This guide outlines the steps to create your free Databricks account and start working in a notebook.

### 1. Account Registration

1.  **Email Requirement:** Create a new Gmail account or use your existing one.
2.  **Go to Signup Page:** Navigate to the Databricks Free Edition signup page: **`https://login.databricks.com/signup`**
3.  **Complete Signup:**
    * Sign up for an account.
    * The quickest option is to select **"Continue with Google"**.
4.  **Select Free Edition:** On the next screen, look for the option for personal use and select **"Get Free Edition"**.

### 2. Accessing Your Workspace

1.  **Navigate to Workspace:** After your account is created and your workspace is provisioned, go to the main **Workspace** view.
2.  **Create Your Notebook:** Click to **Create a notebook** to start writing and running your first code (Python, SQL, R, or Scala).

> **💡 Note for Future Login:**
> You can directly log in to your account management console going forward:
> **`https://accounts.cloud.databricks.com/login`**

***

## 3. Databricks – GitHub Integration for Collaboration & Code Commit

These steps guide you on how to link your Databricks workspace with your GitHub account to enable code commitment and collaboration.

### Step 1: Link GitHub in Databricks

This step establishes the authorization between the two platforms.

1.  **Open Databricks Workspace:** Log in to your Databricks account: `https://accounts.cloud.databricks.com/login`
2.  **Access Settings:**
    * Click your **user profile icon** (located in the top-right corner).
    * Select **Settings**.
3.  **Go to Linked Accounts:** In the Settings panel, navigate to the **Linked Accounts** section. 
4.  **Add Git Credential:** Click the button **"Add Git credential"**.
5.  **Authorize:** Select the option **"Link Git Account"** $\rightarrow$ **Authorize Databricks** $\rightarrow$ **Configure in GitHub**. (Alternatively, you can use a Personal Access Token created in GitHub.)

### Step 2: Create a New GitHub Repository (If Needed)

If you haven't already, create the repository you intend to link.

1.  **Log in to GitHub:** Go to `https://github.com` and log into your account.
2.  **Create Repository:** Create a **New Repository**. For best practice, initialize it by selecting the **`README.md`** file option.

### Step 3: Install the Databricks GitHub App

This installation grants Databricks the specific permissions required to interact with your repository.

1.  **Open the App Page:** Navigate to the Databricks app on the GitHub marketplace: `https://github.com/apps/databricks`
2.  **Install/Configure:** Click the **Install/Configure** button.
3.  **Verify:** Enter your password to verify your GitHub account.
4.  **Configure Access:**
    * Choose **"Only select repositories"**.
    * Add the repository you created (or plan to use).
    * Click **Install** (or Save).

### Step 4: Creating a Git Folder (Repo) in Databricks

This step connects the cloud notebook environment to the linked GitHub repository.

1.  **Return to Databricks:** Go back to your Databricks workspace.
2.  **Create Git Folder:**
    * Under the **Workspace** section, **right-click** in the desired location.
    * Select **Create** $\rightarrow$ **Git Folder**. A pop-up window will appear.
3.  **Link Repository:**
    * Copy the newly created GitHub **HTTP URL** for your repository.
    * Paste it into the **Git Repo URL** field in Databricks.
    * Provide a local **Repo Name** for the folder in Databricks.
    * Click **Create Git Folder**.
4.  **Done!** Your Databricks workspace is now synced with your GitHub repository.

***
