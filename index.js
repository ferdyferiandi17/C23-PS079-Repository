import express from "express";
import dotenv from "dotenv";
import cookieParser from "cookie-parser";
import db from "./config/Database.js";
import router from "./routes/index.js";
import cors from "cors";
dotenv.config();
const app = express();

try {
    await db.authenticate();
    console.log('database connected'); 
} catch (error) {
    console.log(error)
}

app.use(cors({credentials: true, origin:"//untuk api yang mengakses jika react localhost 3000"}))
app.use(cookieParser());
app.use(express.json());
app.use(router);

app.listen(7000, ()=> console.log('server berjalan di port 7000'));