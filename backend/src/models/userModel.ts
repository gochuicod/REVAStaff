import { Document, Schema, model } from 'mongoose';
import bcrypt from 'bcryptjs'

export enum Role {
  User="user",
  Admin="admin",
  Developer="developer"
}

export interface IUser extends Document {
  username: string;
  firstname: string;
  lastname: string;
  password: string;
  role: Role;
  created_at: Date;
  updated_at: Date;
}

const UserSchema: Schema = new Schema({
  username: {
    type: String,
    required: true,
    unique: true
  },
  firstname: {
    type: String,
    required: true,
  },
  lastname: {
    type: String,
    required: true,
  },
  password: {
    type: String,
    required: true,
  },
  role: {
    type: String,
    enum: Object.values(Role),
    default: Role.User,
    required: false
  },
  created_at: {
    type: Date,
    default: Date.now(),
    required: false
  },
  updated_at: {
    type: Date,
    default: Date.now(),
    required: false
  }
});

UserSchema.pre<IUser>('save', async function(next) {
  if (!this.isModified('password')) {
    return next();
  }
  const salt = await bcrypt.genSalt(10);
  this.password = await bcrypt.hash(this.password, salt);
  next();
});

const User = model<IUser>('User', UserSchema);

export default User;