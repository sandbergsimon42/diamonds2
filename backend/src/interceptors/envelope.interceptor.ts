import {
  Injectable,
  NestInterceptor,
  ExecutionContext,
  CallHandler,
} from "@nestjs/common";
import { Observable } from "rxjs";
import { map } from "rxjs/operators";

export interface Response<T> {
  data: T;
}

@Injectable()
export class EnvelopeInterceptor<T> implements NestInterceptor<T, Response<T>> {
  constructor(private logger) {}

  intercept(
    context: ExecutionContext,
    next: CallHandler,
  ): Observable<Response<T>> {
    const req = context.getArgByIndex(0);
    const res = context.getArgByIndex(1);

    return next.handle().pipe(
      map(data => {
        return {
          statusCode: res.status,
          timestamp: new Date().toISOString(),
          path: req.url,
          data,
        };
      }),
    );
  }
}
