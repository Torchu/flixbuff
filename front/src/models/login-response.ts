import { Expose, Type } from 'class-transformer';
import { User } from './user';

export class LoginResponse {
  @Expose({ name: 'access_token' }) accessToken: string;

  @Expose({ name: 'login_ok' }) loginOk: boolean;

  @Type(() => User) user: User;

  constructor(accessToken: string, loginOk: boolean, user: User) {
    this.accessToken = accessToken;
    this.loginOk = loginOk;
    this.user = user;
  }
}
