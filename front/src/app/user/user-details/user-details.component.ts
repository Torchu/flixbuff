import { Component, OnInit } from '@angular/core';
import { Review, ReviewList } from 'src/models/review';
import { ActivatedRoute } from '@angular/router';
import { User } from 'src/models/user';
import { UserService } from 'src/services/user.service';

@Component({
  selector: 'app-user-details',
  templateUrl: './user-details.component.html',
  styleUrls: ['./user-details.component.scss']
})
export class UserDetailsComponent implements OnInit {
  reviewList: Array<Review>;
  user: User;

  constructor(private userService: UserService, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      this.userService.getReviews(params['id']).subscribe((reviewList: ReviewList) => {
        this.reviewList = reviewList.items;
      });
      this.userService.get(params['id']).subscribe((user) => {
        this.user = user;
      });
    });
  }
}
