import { Component, OnInit } from '@angular/core';
import { User, UserList } from 'src/models/user';
import { debounceTime, switchMap } from 'rxjs';
import { FormControl } from '@angular/forms';
import { Router } from '@angular/router';
import { UserService } from 'src/services/user.service';

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.scss']
})
export class UserListComponent implements OnInit {
  searchBar: FormControl;
  userList: Array<User> = [];

  constructor(private userService: UserService, private router: Router) {
    this.searchBar = new FormControl('');
  }

  ngOnInit(): void {
    // Initial load
    this.userService.list().subscribe((userList: UserList) => {
      this.userList = userList.items;
    });

    this.searchBar.valueChanges
      .pipe(
        debounceTime(500),
        switchMap((value: string) => this.userService.list(value))
      )
      .subscribe((users: UserList) => {
        this.userList = users.items;
      });
  }

  /**
   * Open the details of the selected user
   * @param {string} userId ID of the user to open
   */
  openUserDetails(userId: string): void {
    this.router.navigate(['users', userId]);
  }
}
