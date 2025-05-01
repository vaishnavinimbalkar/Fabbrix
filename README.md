**FABBRIX**

**Description**
**FABBRIX** is an ML-driven discount offer system integrated into an e-commerce website. The project leverages machine learning to provide personalized discount offers to users, enhancing the shopping experience and boosting sales.

**Features**
- 🎯 Machine learning-based discount prediction and offers  
- 🛒 Full-stack e-commerce functionalities including product listing, cart, and order management  
- 💳 Integration with payment gateways (Stripe)  
- 🔐 User authentication and authorization  
- 💻 Responsive and modern frontend built with React and Tailwind CSS  
- 🧩 RESTful API backend with Express and PostgreSQL  
- 📚 API documentation with Swagger  
- ✅ Server-side testing with Jest and Supertest  

**Tech Stack**

Frontend
- React  
- Vite  
- Tailwind CSS  
- React Router  
- Stripe  
- Axios  

Backend
- Node.js  
- Express  
- PostgreSQL  
- JWT (JSON Web Tokens)  
- Stripe  
- Swagger  
- Pino Logger  

Machine Learning
- Python scripts for discount prediction integrated into the system

Testing
- Jest  
- Supertest  

**Installation**

Clone the repository:
```bash
git clone <repository-url>
cd FABBRIX
```

Install dependencies for the server:
```bash
cd server
npm install
```

Install dependencies for the client:
```bash
cd ../client
npm install
```

**Running the Project**

Run both client and server concurrently in development mode:
```bash
npm run dev
```

Run the server only:
```bash
npm run server
```

Run the client only:
```bash
npm run client
```

**Testing**

To run server tests:
```bash
cd server
npm test
```

**Folder Structure**
```
FABBRIX/
├── client/        # React frontend application
├── server/        # Express backend API server
├── ML_code/       # Machine learning scripts and models for discount prediction
└── ...            # Root project files and configuration
```

**Environment Variables**
Create a `.env` file in the `server/` directory with the following:
```
DB_USER=your_db_user
DB_HOST=localhost
DB_NAME=your_db_name
DB_PASS=your_db_password
DB_PORT=5432
JWT_SECRET=your_jwt_secret
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
```

**Contact**
**Vaishnavi Nimbalkar**  
📧 Email: [vaishnavi.nimbalkar26@gmail.com](mailto:vaishnavi.nimbalkar26@gmail.com)  
🌐 GitHub: [vaishnavinimbalkar](https://github.com/vaishnavinimbalkar)

**Acknowledgements**
- Base code adapted from **PERN-Store**  
- Machine learning code and system integration developed by the **project team**
