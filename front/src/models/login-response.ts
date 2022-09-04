import { Expose, Type } from 'class-transformer';

export class UserData {
  @Expose() id: string;

  @Expose() email: string;

  @Expose() username: string;

  constructor(id: string, email: string, username: string) {
    this.id = id;
    this.email = email;
    this.username = username;
  }
}

export class LoginResponse {
  @Expose({ name: 'access_token' }) accessToken: string;

  @Expose({ name: 'login_ok' }) loginOk: boolean;

  @Type(() => UserData) user: UserData;

  constructor(accessToken: string, loginOk: boolean, user: UserData) {
    this.accessToken = accessToken;
    this.loginOk = loginOk;
    this.user = user;
  }
}
