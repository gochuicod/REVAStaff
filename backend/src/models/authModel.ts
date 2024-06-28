import { Schema, model } from "mongoose";

export interface IAuth {
  username: string;
  password: boolean;
}

const AuthSchema: Schema = new Schema ({
  username: {
    type: String,
    required: true
  },
  password: {
    type: String,
    required: true
  }
})

const Auth = model<IAuth>('Auth', AuthSchema)

export default Auth