import { Component, OnInit } from '@angular/core';
import { Review, ReviewList } from 'src/models/review';
import { Show, ShowList } from 'src/models/show';
import { ReviewService } from 'src/services/review.service';
import { Router } from '@angular/router';
import { ShowService } from 'src/services/show.service';

@Component({
  selector: 'app-feed',
  templateUrl: './feed.component.html',
  styleUrls: ['./feed.component.scss']
})
export class FeedComponent implements OnInit {
  popularShowList: Array<Show> = [];
  latestReviewList: Array<Review> = [];
  currentPage = 0;

  constructor(private router: Router, private showService: ShowService, private reviewService: ReviewService) {}

  ngOnInit(): void {
    this.showService.getPopular().subscribe((shows: ShowList) => {
      this.popularShowList = shows.items;
    });
    this.reviewService.list().subscribe((reviews: ReviewList) => {
      this.latestReviewList = reviews.items;
    });
  }

  /**
   * Open the show details page
   * @param showId The show id
   */
  openDetails(showId: number): void {
    this.router.navigate(['shows', showId]);
  }

  /**
   * Gets the page of the list
   * @param page The page
   * @returns {Array<Show>} The page
   */
  getShowsPaginated(page: number): Array<Show> {
    const pageSize = 5;
    return this.popularShowList.slice(page * pageSize, (page + 1) * pageSize);
  }

  previous(): void {
    this.currentPage--;
  }

  next(): void {
    this.currentPage++;
  }
}
