import express from 'express';
import connectDB from './config/database';
import dotenv from 'dotenv';
import cors from 'cors'

import userRouter from './routes/userRoutes';
import authRouter from './routes/authRoutes';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

connectDB();

app.use(cors({
  credentials: true,
  origin: "https://revastaff.vercel.app",
  methods: ["GET","POST","PATCH","DELETE"],
  allowedHeaders: ["X-CSRF-Token", "X-Requested-With", "Accept", "Accept-Version", "Content-Length", "Content-MD5", "Content-Type", "Date", "X-Api-Version"]
}))

app.use(express.json());

app.use('/api/users', userRouter);
app.use('/api/auth', authRouter);

app.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`)
})

export default app